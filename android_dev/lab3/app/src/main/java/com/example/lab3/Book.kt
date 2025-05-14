package com.example.lab3

data class Book(
    var title: String,
    var author: String,
    var review: String,
    var rating: Float,
    var genres: List<String>
)
