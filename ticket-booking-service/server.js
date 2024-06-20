const express = require('express');
const bodyParser = require('body-parser');
const { Sequelize, DataTypes } = require('sequelize');

const app = express();
app.use(bodyParser.json());

const sequelize = new Sequelize(process.env.DATABASE_URL, {
  dialect: 'postgres',
  protocol: 'postgres',
  dialectOptions: {
    ssl: {
      require: true,
      rejectUnauthorized: false
    }
  }
});

// Skema Database
const Booking = sequelize.define('Booking', {
  type: {
    type: DataTypes.STRING,
    allowNull: false
  },
  name: {
    type: DataTypes.STRING,
    allowNull: false
  },
  date: {
    type: DataTypes.DATE,
    allowNull: false
  },
  details: {
    type: DataTypes.STRING,
    allowNull: false
  }
});

// Sinkronisasi Database
sequelize.sync();

// Operasi CRUD
app.get('/bookings', async (req, res) => {
  const bookings = await Booking.findAll();
  res.json(bookings);
});

app.post('/bookings', async (req, res) => {
  const booking = await Booking.create(req.body);
  res.json(booking);
});

app.put('/bookings/:id', async (req, res) => {
  const booking = await Booking.findByPk(req.params.id);
  if (booking) {
    await booking.update(req.body);
    res.json(booking);
  } else {
    res.status(404).json({ error: 'Booking not found' });
  }
});

app.delete('/bookings/:id', async (req, res) => {
  const booking = await Booking.findByPk(req.params.id);
  if (booking) {
    await booking.destroy();
    res.json({ message: 'Booking deleted' });
  } else {
    res.status(404).json({ error: 'Booking not found' });
  }
});

// Mulai server
app.listen(3000, () => {
  console.log('Ticket Booking Service running on port 3000');
});
