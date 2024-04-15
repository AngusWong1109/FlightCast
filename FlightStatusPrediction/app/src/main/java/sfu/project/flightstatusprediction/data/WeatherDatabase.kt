package sfu.project.flightstatusprediction.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [Weather::class], version = 1)
abstract class WeatherDatabase : RoomDatabase() {
    abstract val weatherDatabaseDao: WeatherDatabaseDao

    companion object{
        @Volatile
        private var INSTANCE: WeatherDatabase? = null

        fun getInstance(context: Context) : WeatherDatabase{
            synchronized(this){
                var instance = INSTANCE
                if(instance == null){
                    instance = Room.databaseBuilder(context.applicationContext, WeatherDatabase::class.java, "Weather_table").build()
                    INSTANCE = instance
                }
                return instance
            }
        }
    }
}