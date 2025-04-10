package com.example.lab2

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class NotificationAdapter(
    private var notifications: List<Notification>
) : RecyclerView.Adapter<NotificationAdapter.ViewHolder>() {

    fun updateData(newData: List<Notification>) {
        notifications = newData
        notifyDataSetChanged()
    }

    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val messageText: TextView = view.findViewById(android.R.id.text1)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(android.R.layout.simple_list_item_1, parent, false)
        return ViewHolder(view)
    }

    override fun getItemCount(): Int = notifications.size

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val notification = notifications[position]
        holder.messageText.text = "${notification.message} (${notification.importance})"

        // Кольори за рівнем важливості
        val color = when (notification.importance) {
            ImportanceLevel.HIGH -> Color.RED
            ImportanceLevel.MEDIUM -> Color.YELLOW
            ImportanceLevel.LOW -> Color.GREEN
        }
        holder.messageText.setTextColor(color)
    }
}