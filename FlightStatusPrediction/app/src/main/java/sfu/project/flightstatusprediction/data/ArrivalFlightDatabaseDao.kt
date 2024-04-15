package sfu.project.flightstatusprediction.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface ArrivalFlightDatabaseDao {
    @Insert
    suspend fun insertFlight(arrivalFlight: DBArrFlightInfo)

    @Query("SELECT * FROM Arrival_Flight")
    fun getAllArrivalFlights(): Flow<List<DBArrFlightInfo>>

    @Query("SELECT * FROM Arrival_Flight WHERE date_column = :date")
    fun getArrivalFlightsAt(date: String): Flow<List<DBArrFlightInfo>>

    @Query("DELETE FROM Arrival_Flight")
    suspend fun deleteAll()

    @Query("DELETE FROM Arrival_Flight WHERE id = :key")
    suspend fun deleteArrivalFlight(key: Long)
}