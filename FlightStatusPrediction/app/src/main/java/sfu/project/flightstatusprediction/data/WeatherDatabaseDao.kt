package sfu.project.flightstatusprediction.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface WeatherDatabaseDao {
    @Insert
    suspend fun insertWeatherInfo(weather: Weather)

    @Query("SELECT * FROM Weather_table")
    fun getAllWeather(): Flow<List<Weather>>

    @Query("SELECT * FROM Weather_table WHERE date_column = :date AND time_column = :time")
    fun getWeatherAt(date: String, time: String): Weather

    @Query("DELETE FROM Weather_table")
    suspend fun deleteAll()

    @Query("DELETE FROM Weather_table WHERE id = :key")
    suspend fun deleteWeather(key: Long)
}