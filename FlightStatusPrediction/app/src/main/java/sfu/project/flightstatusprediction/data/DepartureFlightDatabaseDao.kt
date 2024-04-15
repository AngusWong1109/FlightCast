package sfu.project.flightstatusprediction.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface DepartureFlightDatabaseDao {
    @Insert
    suspend fun insertFlight(departureFlight: DBDepFlightInfo)

    @Query("SELECT * FROM Departure_Flight")
    fun getAllDepartureFlights(): Flow<List<DBDepFlightInfo>>

    @Query("SELECT * FROM Departure_Flight WHERE date_column = :date")
    fun getDepartureFlightsAt(date: String): Flow<List<DBDepFlightInfo>>

    @Query("DELETE FROM Departure_Flight")
    suspend fun deleteAll()

    @Query("DELETE FROM Departure_Flight WHERE id = :key")
    suspend fun deleteDepartureFlight(key: Long)
}