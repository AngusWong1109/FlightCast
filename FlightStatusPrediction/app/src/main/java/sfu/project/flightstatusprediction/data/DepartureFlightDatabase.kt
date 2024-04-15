package sfu.project.flightstatusprediction.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities=  [DBDepFlightInfo::class], version = 1)
abstract class DepartureFlightDatabase : RoomDatabase() {
    abstract val departureFlightDatabaseDao: DepartureFlightDatabaseDao

    companion object{
        @Volatile
        private var INSTANCE: DepartureFlightDatabase? = null

        fun getInstance(context: Context) : DepartureFlightDatabase{
            synchronized(this){
                var instance = INSTANCE
                if(instance == null){
                    instance = Room.databaseBuilder(context.applicationContext, DepartureFlightDatabase::class.java, "Departure_Flight").build()
                    INSTANCE = instance
                }
                return instance
            }
        }
    }
}