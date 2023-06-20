import Bard, { askAI } from "bard-ai";

import dotenv from "dotenv";

dotenv.config();

// Retrieve the API key from the environment variables  file
const apiKey = process.env.BARD_API_KEY;

await Bard.init(apiKey);

// Create a list of data
const data = [
    {
        name: 'John',
        age: 30,
        city: 'New York'
    },
    {
        name: 'Peter',
        age: 40,
        city: 'Boston'
    }
];



const prompt2 = 'From the data list provided at the end, your response should not be in JSON format and it should be concise.';

 console.log(await Bard.askAI("find all the names whose age is greater than 30 from the given data list: " +  data ));

