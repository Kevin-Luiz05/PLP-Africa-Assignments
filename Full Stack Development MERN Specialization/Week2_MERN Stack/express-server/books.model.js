// models/book.model.js
const mongoose = require('mongoose');

const BookSchema = new mongoose.Schema({
  title: { type: String, required: true, index: true },
  author: { type: String, required: true, index: true },
  genre: { type: String, required: true, index: true },
  published_year: { type: Number, required: true, index: true },
  price: { type: Number, required: true },
  in_stock: { type: Boolean, default: true },
  pages: { type: Number },
  publisher: { type: String }
}, { timestamps: true });

// Compound index example
BookSchema.index({ author: 1, published_year: -1 });

module.exports = mongoose.model('Book', BookSchema);
