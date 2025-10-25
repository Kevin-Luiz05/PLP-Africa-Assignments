// routes/books.routes.js
const express = require('express');
const { body } = require('express-validator');
const router = express.Router();
const controller = require('../controllers/books.controller');
const { validate } = require('../middleware/validate.middleware');

// CRUD
router.post('/',
  [
    body('title').isString().notEmpty(),
    body('author').isString().notEmpty(),
    body('genre').isString().notEmpty(),
    body('published_year').isInt({ min: 0 }),
    body('price').isFloat({ min: 0 })
  ],
  validate,
  controller.createBook
);

router.get('/', controller.getBooks);
router.get('/aggregations/avg-by-genre', controller.avgPriceByGenre);
router.get('/aggregations/top-author', controller.topAuthor);
router.get('/aggregations/by-decade', controller.groupByDecade);

router.get('/:id', controller.getBookById);
router.put('/:id',
  [
    body('title').optional().isString(),
    body('author').optional().isString(),
    body('genre').optional().isString(),
    body('published_year').optional().isInt({ min: 0 }),
    body('price').optional().isFloat({ min: 0 })
  ],
  validate,
  controller.updateBook
);
router.patch('/:id', controller.partialUpdateBook);
router.delete('/:id', controller.deleteBook);

module.exports = router;
