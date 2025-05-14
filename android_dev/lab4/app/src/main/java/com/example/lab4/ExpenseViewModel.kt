package com.example.lab4

import androidx.lifecycle.ViewModel

class ExpenseViewModel : ViewModel() {
    private val _expenses = mutableListOf<Float>()
    val expenses: List<Float> get() = _expenses

    fun addExpense(amount: Float) {
        _expenses.add(amount)
    }
}
