using System;                   // Provides core functionality like input/output and data types
using System.Net.Http;          // Enables sending HTTP requests to APIs
using System.Threading.Tasks;   // Supports asynchronous programming to keep the app responsive
using Newtonsoft.Json.Linq;     // Helps parse and manipulate JSON data

class Program
{
    static async Task Main(string[] args)
    {
        // Define the API URL, including the parameters for latitude, longitude, and requested data.
        string apiUrl = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m";

        using (HttpClient client = new HttpClient())
        {
            HttpResponseMessage response = await client.GetAsync(apiUrl);

            if (response.IsSuccessStatusCode)
            {
                string json = await response.Content.ReadAsStringAsync();
                var data = JObject.Parse(json);

                // Display entire JSON payload
                Console.WriteLine("Full API Response:");
                Console.WriteLine(json);

                // Display 7-day forecast summary
                Console.WriteLine("\n7-Day Forecast:");
                var temperatures = data["hourly"]["temperature_2m"];
                var times = data["hourly"]["time"];

                for (int i = 0; i < 168; i += 24) // Display one temperature per day
                {
                    Console.WriteLine($"Date: {times[i]} - Temp: {temperatures[i]}°C");
                }
            }
            else
            {
                Console.WriteLine("Error: Unable to fetch data.");
            }
        }
    }
}