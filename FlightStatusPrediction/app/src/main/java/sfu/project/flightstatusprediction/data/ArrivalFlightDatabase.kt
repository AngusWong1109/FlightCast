package sfu.project.flightstatusprediction.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [DBArrFlightInfo::class], version = 1)
abstract class ArrivalFlightDatabase : RoomDatabase() {
    abstract val arrivalFlightDatabaseDao: ArrivalFlightDatabaseDao

    companion object{
        @Volatile
        private var INSTANCE: ArrivalFlightDatabase? = null

        fun getInstance(context: Context) : ArrivalFlightDatabase{
            synchronized(this){
                var instance = INSTANCE
                if(instance == null){
                    instance = Room.databaseBuilder(context.applicationContext, ArrivalFlightDatabase::class.java, "Arrival_Flight").build()
                    INSTANCE = instance
                }
                return instance
            }
        }
    }
}