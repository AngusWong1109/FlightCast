package sfu.project.flightstatusprediction

import android.app.Activity
import android.content.Intent
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import sfu.project.flightstatusprediction.data.DBArrFlightInfo

class ArrFlightListAdapter(): RecyclerView.Adapter<FlightViewHolder>(){
    companion object{
        var flights: List<DBArrFlightInfo> = ArrayList()
    }
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): FlightViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.flight_list_recycler_view_layout, parent, false)
        return FlightViewHolder(view)
    }

    override fun getItemCount(): Int {
        return flights.size
    }

    override fun onBindViewHolder(holder: FlightViewHolder, position: Int) {
        val flightListInfo = flights[position]
        holder.tvTime.text = flightListInfo.time
        holder.tvFlightNo.text = flightListInfo.flightNo
        holder.tvStatus.text = flightListInfo.status
        holder.tvPlace.text = flightListInfo.origin
        val activity = holder.itemView.context as Activity
        holder.itemView.setOnClickListener {
            val intent = Intent(activity, ArrivalShowFlightInfoActivity::class.java)
            intent.putExtra(ArrivalShowFlightInfoActivity.ARRIVAL_EXTRA_POSITION, position)
            activity.startActivity(intent)
        }
    }

    fun replace(newFlights: List<DBArrFlightInfo>){
        flights = newFlights
    }
}