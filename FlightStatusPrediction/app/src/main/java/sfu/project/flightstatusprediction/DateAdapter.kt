package sfu.project.flightstatusprediction

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.launch
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModel
import sfu.project.flightstatusprediction.data.DepartureFlightViewModel
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class DateAdapter(private val dataSet: ArrayList<LocalDate>, private val tvSelectedDate: TextView, private val isArrival: Boolean, private val arrivalVM: ArrivalFlightViewModel, private val departureVM: DepartureFlightViewModel): RecyclerView.Adapter<DateAdapter.DateViewHolder>() {
    private var selectedItemPos: Int = 0
    class DateViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val day: TextView
        val date: TextView

        init {
            day = view.findViewById(R.id.tv_day)
            date = view.findViewById(R.id.tv_date)
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DateViewHolder {
        // Create a new view, which defines the UI of the list item
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.date_recycler_view_layout, parent, false)
        return DateViewHolder(view)
    }

    override fun getItemCount(): Int {
        return dataSet.size
    }

    override fun onBindViewHolder(holder: DateViewHolder, position: Int) {
        // Get element from your dataset at this position and replace the
        // contents of the view with that element
        val day = dataSet[position].dayOfWeek
        val dayString = when(day){
            DayOfWeek.MONDAY -> "MON"
            DayOfWeek.TUESDAY -> "TUE"
            DayOfWeek.WEDNESDAY -> "WED"
            DayOfWeek.THURSDAY -> "THU"
            DayOfWeek.FRIDAY -> "FRI"
            DayOfWeek.SATURDAY -> "SAT"
            else -> "SUN"
        }
        val dayOfMonthString = dataSet[position].dayOfMonth.toString()
        val monthString = dataSet[position].monthValue.toString()
        val dateStr = "$dayOfMonthString/$monthString"
        holder.day.text = dayString
        holder.date.text = dateStr

        holder.date.setOnClickListener {
            selectedItemPos = holder.layoutPosition
            updateFlightList(selectedItemPos)
        }
    }

    private fun updateFlightList(selectedItemPos: Int) {
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        val dateString = dataSet[selectedItemPos].format(formatter)
        tvSelectedDate.text = dateString
        if(isArrival){
            CoroutineScope(IO).launch {
                arrivalVM.getArrivalFlightsAt(dateString)
            }
        }
        else{
            CoroutineScope(IO).launch {
                departureVM.getDepartureFlightAt(dateString)
            }
        }
    }
}