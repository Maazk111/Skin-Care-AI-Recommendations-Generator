import express from "express";
import userRoutes from "./routes/users.js";
import aiRoutes from "./routes/users.js";
import dotenv from "dotenv";

const app = express();
app.use(express.json());
dotenv.config();

// User Routes
app.use("/users", userRoutes);

// AI Routes
app.use("/ai", aiRoutes);

const PORT = process.env.PORT || 7653;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
