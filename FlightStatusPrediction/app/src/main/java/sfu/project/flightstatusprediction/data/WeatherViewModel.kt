package sfu.project.flightstatusprediction.data

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.asLiveData
import sfu.project.flightstatusprediction.GetWeatherInfo

class WeatherViewModel(private val repository: WeatherRepository) : ViewModel() {
    val allWeathersLiveData: LiveData<List<Weather>> = repository.allWeathers.asLiveData()

    fun insert(response: GetWeatherInfo.WeatherResponse?){
        if(response == null){
            return
        }
        for (daily in response.days){
            for (hour in daily.hours){
                val weather = Weather()
                weather.date = daily.datetime
                weather.time = hour.datetime
                weather.temp = hour.temp
                weather.feelsLike = hour.feelslike
                weather.dew = hour.dew
                weather.humidity = hour.humidity
                weather.precip = hour.precip
                weather.precipProb = hour.precipprob
                weather.windGust = hour.windgust
                weather.windSpeed = hour.windspeed
                weather.windDir = hour.winddir
                weather.pressure = hour.pressure
                weather.cloudCover = hour.cloudcover
                weather.visibility = hour.visibility
                weather.solarRadiation = hour.solarradiation
                weather.solarEnergy = hour.solarenergy
                weather.uvIndex = hour.uvindex
                weather.severeRisk = hour.severerisk
                weather.conditions = hour.conditions
                repository.insert(weather)
            }
        }
    }

    fun getWeatherAt(date: String, time:String): Weather{
        return repository.getWeatherAt(date, time)
    }

    fun deleteFirst(){
        val weathers = allWeathersLiveData.value
        if(!weathers.isNullOrEmpty()){
            val id = weathers[0].id
            repository.delete(id)
        }
    }

    fun deleteAll(){
        val weathers = allWeathersLiveData.value
        if(!weathers.isNullOrEmpty()){
            repository.deleteAll()
        }
    }
}

class WeatherViewModelFactory (private val repository: WeatherRepository) : ViewModelProvider.Factory{
    override fun<T: ViewModel> create(modelClass: Class<T>) : T{
        if(modelClass.isAssignableFrom(WeatherViewModel::class.java))
            return WeatherViewModel(repository) as T
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}