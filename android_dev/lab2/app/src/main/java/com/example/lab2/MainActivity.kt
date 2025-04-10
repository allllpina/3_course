package com.example.lab2

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

import android.widget.*
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private lateinit var adapter: NotificationAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val messageInput = findViewById<EditText>(R.id.messageInput)
        val importanceSpinner = findViewById<Spinner>(R.id.importanceSpinner)
        val addButton = findViewById<Button>(R.id.addButton)
        val sortButton = findViewById<Button>(R.id.sortButton)
        val clearButton = findViewById<Button>(R.id.clearButton)
        val recyclerView = findViewById<RecyclerView>(R.id.notificationRecycler)

        importanceSpinner.adapter = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_item,
            ImportanceLevel.values()
        )

        adapter = NotificationAdapter(emptyList())
        recyclerView.adapter = adapter
        recyclerView.layoutManager = LinearLayoutManager(this)

        // Кнопка додавання
        addButton.setOnClickListener {
            val message = messageInput.text.toString()
            val importance = importanceSpinner.selectedItem as ImportanceLevel
            if (message.isNotBlank()) {
                NotificationManager.addNotification(message, importance)
                messageInput.text.clear()
            }
        }

        // Сортування
        sortButton.setOnClickListener {
            NotificationManager.sortByImportance()
        }

        // Очистити список
        clearButton.setOnClickListener {
            NotificationManager.clearAll()
        }

        // Спостерігаємо за змінами
        lifecycleScope.launch {
            NotificationManager.notifications.collectLatest { list ->
                adapter.updateData(list)
            }
        }
    }
}