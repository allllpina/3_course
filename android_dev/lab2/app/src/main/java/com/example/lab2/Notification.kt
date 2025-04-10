package com.example.lab2

data class Notification(
    val id: Int,
    val message: String,
    val importance: ImportanceLevel,
    val timestamp: Long = System.currentTimeMillis()
)
