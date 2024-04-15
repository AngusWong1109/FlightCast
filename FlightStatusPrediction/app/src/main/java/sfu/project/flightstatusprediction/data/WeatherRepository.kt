package sfu.project.flightstatusprediction.data

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.launch

class WeatherRepository(private val weatherDatabaseDao: WeatherDatabaseDao) {
    val allWeathers: Flow<List<Weather>> = weatherDatabaseDao.getAllWeather()

    fun getWeatherAt(date: String, time: String): Weather{
        return weatherDatabaseDao.getWeatherAt(date, time)
    }

    fun insert(weather: Weather){
        CoroutineScope(IO).launch {
            weatherDatabaseDao.insertWeatherInfo(weather)
        }
    }

    fun delete(id: Long){
        CoroutineScope(IO).launch {
            weatherDatabaseDao.deleteWeather(id)
        }
    }

    fun deleteAll(){
        CoroutineScope(IO).launch{
            weatherDatabaseDao.deleteAll()
        }
    }
}