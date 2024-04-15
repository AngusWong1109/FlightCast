package sfu.project.flightstatusprediction.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "Departure_Flight")
data class DBDepFlightInfo (
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

    @ColumnInfo(name = "destination_column")
    var destination: String? = "",

    @ColumnInfo(name = "terminal_column")
    var terminal: String? = "",

    @ColumnInfo(name = "aisle_column")
    var aisle: String? = "",

    @ColumnInfo(name = "gate_column")
    var gate: String? = ""
)