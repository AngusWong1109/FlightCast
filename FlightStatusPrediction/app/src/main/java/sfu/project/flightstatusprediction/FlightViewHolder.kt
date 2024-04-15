package sfu.project.flightstatusprediction

import android.view.View
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class FlightViewHolder(view: View) : RecyclerView.ViewHolder(view){
    val tvTime: TextView
    val tvFlightNo: TextView
    val tvStatus: TextView
    val tvPlace: TextView
    init{
        tvTime = view.findViewById(R.id.tv_time)
        tvFlightNo = view.findViewById(R.id.tv_flightNo)
        tvStatus = view.findViewById(R.id.tv_status)
        tvPlace = view.findViewById(R.id.tv_place)
    }
}