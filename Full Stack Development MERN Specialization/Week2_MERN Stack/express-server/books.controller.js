// controllers/books.controller.js
const Book = require('../models/book.model');
const mongoose = require('mongoose');

exports.createBook = async (req, res, next) => {
  try {
    const book = new Book(req.body);
    const saved = await book.save();
    res.status(201).json(saved);
  } catch (err) {
    next(err);
  }
};

exports.getBooks = async (req, res, next) => {
  try {
    // Filtering
    const filter = {};
    if (req.query.genre) filter.genre = req.query.genre;
    if (req.query.author) filter.author = req.query.author;
    if (req.query.in_stock) filter.in_stock = req.query.in_stock === 'true';
    if (req.query.min_year) filter.published_year = { ...(filter.published_year||{}), $gte: Number(req.query.min_year) };
    if (req.query.max_year) filter.published_year = { ...(filter.published_year||{}), $lte: Number(req.query.max_year) };

    // Pagination and sorting
    const limit = Math.max(1, Math.min(100, parseInt(req.query.limit || '10', 10)));
    const page = Math.max(1, parseInt(req.query.page || '1', 10));
    const skip = (page - 1) * limit;
    const sort = req.query.sort || 'title'; // e.g. price,-published_year

    // Build mongoose sort object
    const sortObj = {};
    sort.split(',').forEach(s => {
      s = s.trim();
      if (!s) return;
      if (s.startsWith('-')) sortObj[s.slice(1)] = -1;
      else sortObj[s] = 1;
    });

    const [data, total] = await Promise.all([
      Book.find(filter).sort(sortObj).skip(skip).limit(limit).lean(),
      Book.countDocuments(filter)
    ]);

    res.json({
      page, limit, totalPages: Math.ceil(total / limit), total, data
    });
  } catch (err) {
    next(err);
  }
};

exports.getBookById = async (req, res, next) => {
  try {
    const id = req.params.id;
    if (!mongoose.Types.ObjectId.isValid(id)) return res.status(400).json({ error: 'Invalid id' });
    const book = await Book.findById(id);
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.json(book);
  } catch (err) {
    next(err);
  }
};

exports.updateBook = async (req, res, next) => {
  try {
    const id = req.params.id;
    if (!mongoose.Types.ObjectId.isValid(id)) return res.status(400).json({ error: 'Invalid id' });
    const updated = await Book.findByIdAndUpdate(id, req.body, { new: true, runValidators: true });
    if (!updated) return res.status(404).json({ error: 'Book not found' });
    res.json(updated);
  } catch (err) {
    next(err);
  }
};

exports.partialUpdateBook = async (req, res, next) => {
  try {
    const id = req.params.id;
    if (!mongoose.Types.ObjectId.isValid(id)) return res.status(400).json({ error: 'Invalid id' });
    const updated = await Book.findByIdAndUpdate(id, { $set: req.body }, { new: true, runValidators: true });
    if (!updated) return res.status(404).json({ error: 'Book not found' });
    res.json(updated);
  } catch (err) {
    next(err);
  }
};

exports.deleteBook = async (req, res, next) => {
  try {
    const id = req.params.id;
    if (!mongoose.Types.ObjectId.isValid(id)) return res.status(400).json({ error: 'Invalid id' });
    const deleted = await Book.findByIdAndDelete(id);
    if (!deleted) return res.status(404).json({ error: 'Book not found' });
    res.status(204).end();
  } catch (err) {
    next(err);
  }
};

// Aggregations
exports.avgPriceByGenre = async (req, res, next) => {
  try {
    const pipeline = [
      { $group: { _id: '$genre', averagePrice: { $avg: '$price' }, count: { $sum: 1 } } },
      { $sort: { averagePrice: -1 } }
    ];
    const result = await Book.aggregate(pipeline);
    res.json(result);
  } catch (err) {
    next(err);
  }
};

exports.topAuthor = async (req, res, next) => {
  try {
    const pipeline = [
      { $group: { _id: '$author', count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 1 }
    ];
    const result = await Book.aggregate(pipeline);
    res.json(result[0] || null);
  } catch (err) {
    next(err);
  }
};

exports.groupByDecade = async (req, res, next) => {
  try {
    const pipeline = [
      { $group: {
          _id: { $multiply: [{ $floor: { $divide: ['$published_year', 10] } }, 10] },
          count: { $sum: 1 }
        }
      },
      { $sort: { _id: 1 } }
    ];
    const result = await Book.aggregate(pipeline);
    res.json(result);
  } catch (err) {
    next(err);
  }
};
