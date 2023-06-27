import Bard, { askAI } from "bard-ai";
import dotenv from "dotenv";
import express from "express";
import cors from "cors";

const app = express();
// write your tes
dotenv.config();

// Retrieve the API key from the environment variables file
const apiKey = 'YAjeLuEEFf58g6txvr56-Na_CafiZgXsu6FldB6NY9s31dsT7qIqsJymj7icBcSNuxmhNQ.'
if (!apiKey) {
  console.error("BARD_API_KEY not found in environment variables");
  process.exit(1);
}

(async () => {
  try {
    await Bard.init(apiKey);
    console.log("Bard initialized successfully");
  } catch (error) {
    console.error("Error initializing Bard:", error);
    process.exit(1);
  }
})();

const prompt2 =
  "You are a professional Chatbot integrated into ONE Technology Services' website, a software company offering a wide range of software services. Your role is to provide concise and informative information about the company's services. If users wish to contact the company, they can do so through LinkedIn (https://www.linkedin.com/company/one-technology-services/), Twitter (https://twitter.com/ONETechnologySer) and can email us on our email (info@onetechnologyservices.com). Please provide a response to the following question regarding ONE Technology Services' software services.";

app.use(cors());

app.get("/create-response/:prompt", async (req, res) => {
  const prompt = req.params.prompt;
  try {
    const response = await Bard.askAI(prompt2 + prompt);
    console.log(response);
    res.json({ message: response });
  } catch (error) {
    console.error("Error generating response:", error);
    res.status(500).json({ message: "Error generating response" });
  }
});

app.listen(3000, () => {
  console.log("Server started on port 3000");
});