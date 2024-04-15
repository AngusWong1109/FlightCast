package sfu.project.flightstatusprediction.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "Weather_table")
data class Weather(
    @PrimaryKey(autoGenerate = true)
    var id: Long = 0L,

    @ColumnInfo(name = "date_column")
    var date: String = "",

    @ColumnInfo(name = "time_column")
    var time: String = "",

    @ColumnInfo(name = "temp_column")
    var temp: Double = 0.0,

    @ColumnInfo(name = "feels_like_column")
    var feelsLike: Double = 0.0,

    @ColumnInfo(name = "dew_column")
    var dew: Double = 0.0,

    @ColumnInfo(name = "humidity_column")
    var humidity: Double = 0.0,

    @ColumnInfo(name = "precip")
    var precip: Double? = null,

    @ColumnInfo(name = "precip_prob_column")
    var precipProb: Double? = null,

    @ColumnInfo(name = "windgust_column")
    var windGust: Double = 0.0,

    @ColumnInfo(name = "windspeed_column")
    var windSpeed: Double = 0.0,

    @ColumnInfo(name = "winddir_column")
    var windDir: Double = 0.0,

    @ColumnInfo(name = "pressure_column")
    var pressure: Double = 0.0,

    @ColumnInfo(name = "cloud_cover_column")
    var cloudCover: Double = 0.0,

    @ColumnInfo(name = "visibility_column")
    var visibility: Double = 0.0,

    @ColumnInfo(name = "solar_radiation_column")
    var solarRadiation: Double = 0.0,

    @ColumnInfo(name = "solar_energy_column")
    var solarEnergy: Double = 0.0,

    @ColumnInfo(name = "uv_index_column")
    var uvIndex: Double = 0.0,

    @ColumnInfo(name = "severe_risk_column")
    var severeRisk: Double = 0.0,

    @ColumnInfo(name = "conditions_column")
    var conditions: String = ""
)
