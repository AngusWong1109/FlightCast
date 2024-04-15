package sfu.project.flightstatusprediction

import android.content.res.AssetManager
import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.lifecycle.ViewModelProvider
import androidx.viewpager2.widget.ViewPager2
import com.google.android.material.tabs.TabLayout
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.launch
import sfu.project.flightstatusprediction.data.ArrivalFlightDatabase
import sfu.project.flightstatusprediction.data.ArrivalFlightDatabaseDao
import sfu.project.flightstatusprediction.data.ArrivalFlightRepository
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModel
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModelFactory
import sfu.project.flightstatusprediction.data.DepartureFlightDatabase
import sfu.project.flightstatusprediction.data.DepartureFlightDatabaseDao
import sfu.project.flightstatusprediction.data.DepartureFlightRepository
import sfu.project.flightstatusprediction.data.DepartureFlightViewModel
import sfu.project.flightstatusprediction.data.DepartureFlightViewModelFactory
import sfu.project.flightstatusprediction.data.WeatherDatabase
import sfu.project.flightstatusprediction.data.WeatherDatabaseDao
import sfu.project.flightstatusprediction.data.WeatherRepository
import sfu.project.flightstatusprediction.data.WeatherViewModel
import sfu.project.flightstatusprediction.data.WeatherViewModelFactory
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class HomeActivity : AppCompatActivity() {
    private lateinit var tabLayout: TabLayout
    private lateinit var viewPager: ViewPager2
    private lateinit var fragmentAdapter: FragmentPageAdapter

    private lateinit var arrFlightDb: ArrivalFlightDatabase
    private lateinit var arrFlightDbDao: ArrivalFlightDatabaseDao
    private lateinit var arrFlightRepository: ArrivalFlightRepository
    private lateinit var arrFlightViewModelFactory: ArrivalFlightViewModelFactory
    private lateinit var arrFlightViewModel: ArrivalFlightViewModel

    private lateinit var depFlightDb: DepartureFlightDatabase
    private lateinit var depFlightDbDao: DepartureFlightDatabaseDao
    private lateinit var depFlightRepository: DepartureFlightRepository
    private lateinit var depFlightViewModelFactory: DepartureFlightViewModelFactory
    private lateinit var depFlightViewModel: DepartureFlightViewModel

    private lateinit var weatherDb: WeatherDatabase
    private lateinit var weatherDbDao: WeatherDatabaseDao
    private lateinit var weatherRepository: WeatherRepository
    private lateinit var weatherViewModelFactory: WeatherViewModelFactory
    private lateinit var weatherViewModel: WeatherViewModel
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_home)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        arrFlightDb = ArrivalFlightDatabase.getInstance(this)
        arrFlightDbDao = arrFlightDb.arrivalFlightDatabaseDao
        arrFlightRepository = ArrivalFlightRepository(arrFlightDbDao)
        arrFlightViewModelFactory = ArrivalFlightViewModelFactory(arrFlightRepository)
        arrFlightViewModel = ViewModelProvider(this, arrFlightViewModelFactory).get(ArrivalFlightViewModel::class.java)

        depFlightDb = DepartureFlightDatabase.getInstance(this)
        depFlightDbDao = depFlightDb.departureFlightDatabaseDao
        depFlightRepository = DepartureFlightRepository(depFlightDbDao)
        depFlightViewModelFactory = DepartureFlightViewModelFactory(depFlightRepository)
        depFlightViewModel = ViewModelProvider(this, depFlightViewModelFactory).get(DepartureFlightViewModel::class.java)

        weatherDb = WeatherDatabase.getInstance(this)
        weatherDbDao = weatherDb.weatherDatabaseDao
        weatherRepository = WeatherRepository(weatherDbDao)
        weatherViewModelFactory = WeatherViewModelFactory(weatherRepository)
        weatherViewModel = ViewModelProvider(this, weatherViewModelFactory).get(WeatherViewModel::class.java)

        GetFlightInfo().fetchAllFlight(depFlightViewModel, arrFlightViewModel)
        var weatherResponse: GetWeatherInfo.WeatherResponse? = null
        CoroutineScope(IO).launch{
            weatherResponse = GetWeatherInfo().getWeather()
            weatherViewModel.insert(weatherResponse)
        }

        tabLayout = findViewById(R.id.tabLayout)
        viewPager = findViewById(R.id.viewPager)
        fragmentAdapter = FragmentPageAdapter(supportFragmentManager, lifecycle)

        tabLayout.addTab(tabLayout.newTab().setText("Departure"))
        tabLayout.addTab(tabLayout.newTab().setText("Arrival"))

        viewPager.adapter = fragmentAdapter

        tabLayout.addOnTabSelectedListener(object: TabLayout.OnTabSelectedListener{
            override fun onTabSelected(tab: TabLayout.Tab?) {
                viewPager.currentItem = tab!!.position
            }

            override fun onTabUnselected(p0: TabLayout.Tab?) {

            }

            override fun onTabReselected(p0: TabLayout.Tab?) {

            }
        })

        viewPager.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback(){
            override fun onPageSelected(position: Int) {
                super.onPageSelected(position)
                tabLayout.selectTab(tabLayout.getTabAt(position))
            }
        })
    }
}