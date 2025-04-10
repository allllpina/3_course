package com.example.lab2

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

object NotificationManager {
    private val _notifications = MutableStateFlow<List<Notification>>(emptyList())
    val notifications: StateFlow<List<Notification>> = _notifications

    private var nextId = 0
    private val scope = CoroutineScope(Dispatchers.Default + SupervisorJob())

    fun addNotification(message: String, importance: ImportanceLevel) {
        val notification = Notification(nextId++, message, importance)
        _notifications.value = _notifications.value + notification

        // Автоматичне видалення через 10 секунд
        scope.launch {
            delay(10_000)
            removeNotification(notification.id)
        }
    }

    fun removeNotification(id: Int) {
        _notifications.value = _notifications.value.filterNot { it.id == id }
    }

    fun clearAll() {
        _notifications.value = emptyList()
    }

    fun sortByImportance() {
        _notifications.value = _notifications.value.sortedBy { it.importance }
    }
}