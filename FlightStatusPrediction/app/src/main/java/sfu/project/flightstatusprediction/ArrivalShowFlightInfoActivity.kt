package sfu.project.flightstatusprediction

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.lifecycle.ViewModelProvider
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.launch
import sfu.project.flightstatusprediction.data.DBArrFlightInfo
import sfu.project.flightstatusprediction.data.Weather
import sfu.project.flightstatusprediction.data.WeatherDatabase
import sfu.project.flightstatusprediction.data.WeatherDatabaseDao
import sfu.project.flightstatusprediction.data.WeatherRepository
import sfu.project.flightstatusprediction.data.WeatherViewModel
import sfu.project.flightstatusprediction.data.WeatherViewModelFactory
import sfu.project.flightstatusprediction.data.TripInfo

class ArrivalShowFlightInfoActivity : AppCompatActivity() {
    companion object{
        const val ARRIVAL_EXTRA_POSITION = "arrival position"
        const val SHOW_HYPHEN = "-"
    }

    private lateinit var weatherDb: WeatherDatabase
    private lateinit var weatherDbDao: WeatherDatabaseDao
    private lateinit var weatherRepository: WeatherRepository
    private lateinit var weatherViewModelFactory: WeatherViewModelFactory
    private lateinit var weatherViewModel: WeatherViewModel

    private lateinit var tvDate: TextView
    private lateinit var tvTime: TextView
    private lateinit var tvFlightNo: TextView
    private lateinit var tvAirline: TextView
    private lateinit var tvOrigin: TextView
    private lateinit var tvBaggage: TextView
    private lateinit var tvTerminal: TextView
    private lateinit var tvHall: TextView
    private lateinit var labelPredict: TextView
    private lateinit var tvPredict: TextView
    private lateinit var btnPredict: Button

    private var position: Int = 0
    private lateinit var flightInfo: DBArrFlightInfo
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_arrival_show_flight_info)

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        weatherDb = WeatherDatabase.getInstance(this)
        weatherDbDao = weatherDb.weatherDatabaseDao
        weatherRepository = WeatherRepository(weatherDbDao)
        weatherViewModelFactory = WeatherViewModelFactory(weatherRepository)
        weatherViewModel = ViewModelProvider(this, weatherViewModelFactory).get(WeatherViewModel::class.java)

        tvDate = findViewById(R.id.tv_arrFlightInfoDate)
        tvTime = findViewById(R.id.tv_arrFlightInfoTime)
        tvFlightNo = findViewById(R.id.tv_arrFlightInfoFlightNo)
        tvAirline = findViewById(R.id.tv_arrFlightInfoAirline)
        tvOrigin = findViewById(R.id.tv_ArrFlightInfoOrigin)
        tvBaggage = findViewById(R.id.tv_arrFlightInfoBaggage)
        tvTerminal = findViewById(R.id.tv_arrFlightInfoTerminal)
        tvHall = findViewById(R.id.tv_arrFlightInfoHall)
        labelPredict = findViewById(R.id.label_predict)
        tvPredict = findViewById(R.id.tv_arrFlightInfoPredict)
        btnPredict = findViewById(R.id.btn_arrFlightInfoPredict)

        position = intent.getIntExtra(ARRIVAL_EXTRA_POSITION, 0)
        flightInfo = ArrFlightListAdapter.flights[position]

        var weather = Weather()
        CoroutineScope(IO).launch{
            weather = weatherViewModel.getWeatherAt(flightInfo.date, flightInfo.time)
        }

        tvDate.text = flightInfo.date
        tvTime.text = flightInfo.time
        tvFlightNo.text = flightInfo.flightNo
        tvAirline.text = flightInfo.airline
        tvOrigin.text = flightInfo.origin
        if(flightInfo.baggage == null || flightInfo.baggage == ""){
            tvBaggage.text = SHOW_HYPHEN
        }
        if(flightInfo.terminal == null || flightInfo.terminal == ""){
            tvTerminal.text = SHOW_HYPHEN
        }
        if(flightInfo.hall == null || flightInfo.hall == ""){
            tvHall.text = SHOW_HYPHEN
        }

        btnPredict.setOnClickListener {
            labelPredict.visibility = View.VISIBLE
            tvPredict.visibility = View.VISIBLE
            val data = TripInfo(
                weather.time,
                flightInfo.flightNo,
                flightInfo.airline,
                flightInfo.origin,
                weather.temp,
                weather.feelsLike,
                weather.dew,
                weather.humidity,
                weather.precip,
                weather.precipProb,
                weather.windGust,
                weather.windSpeed,
                weather.windDir,
                weather.pressure,
                weather.cloudCover,
                weather.visibility,
                weather.solarRadiation,
                weather.solarEnergy,
                weather.uvIndex,
                weather.severeRisk,
                weather.conditions
            )

            if(! Python.isStarted()){
                Python.start(AndroidPlatform(this))
            }
            val py = Python.getInstance()
            val module = py.getModule("arr_model")
            val predictFunc = module["predict"]
            val result = predictFunc?.call(data)
            tvPredict.text = result.toString()
        }
    }
}