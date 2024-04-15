package sfu.project.flightstatusprediction.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "Arrival_Flight")
data class DBArrFlightInfo(
    @PrimaryKey(autoGenerate = true)
    var id: Long = 0L,

    @ColumnInfo(name = "date_column")
    var date: String = "",

    @ColumnInfo(name = "arrival_column")
    var arrival: Boolean = true,

    @ColumnInfo(name = "cargo_column")
    var cargo: Boolean = false,

    @ColumnInfo(name = "time_column")
    var time: String = "",

    @ColumnInfo(name = "flight_no_column")
    var flightNo: String? = "",

    @ColumnInfo(name = "airline_column")
    var airline: String? = "",

    @ColumnInfo(name = "status_column")
    var status: String? = null,

    @ColumnInfo(name = "status_code_column")
    var statusCode: String? = null,

    @ColumnInfo(name = "origin_column")
    var origin: String? = "",

    @ColumnInfo(name = "baggage_column")
    var baggage: String? = "",

    @ColumnInfo(name = "hall_column")
    var hall: String? = "",

    @ColumnInfo(name = "terminal_column")
    var terminal: String? = "",

    @ColumnInfo(name = "stand_column")
    var stand: String? = ""
)
