import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class PR3_WeatherAvg {

    public static void main(String[] args) {

        String fileName = "sample_weather.txt";

        int count = 0;

        double tempSum = 0;
        double dewSum = 0;
        double windSum = 0;

        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));

            String line;

            while ((line = br.readLine()) != null) {

                // Skip empty lines
                if (line.trim().isEmpty()) {
                    continue;
                }

                String[] data = line.split("\\s+");

                // Check if line has enough columns
                if (data.length < 4) {
                    System.out.println("Invalid line skipped: " + line);
                    continue;
                }

                double temperature = Double.parseDouble(data[1]);
                double dewPoint = Double.parseDouble(data[2]);
                double windSpeed = Double.parseDouble(data[3]);

                tempSum += temperature;
                dewSum += dewPoint;
                windSum += windSpeed;

                count++;
            }

            br.close();

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Avoid division by zero
        if (count > 0) {
            System.out.println("===== WEATHER ANALYSIS =====");
            System.out.println("Average Temperature : " + (tempSum / count));
            System.out.println("Average Dew Point   : " + (dewSum / count));
            System.out.println("Average Wind Speed  : " + (windSum / count));
        } else {
            System.out.println("No valid data found.");
        }
    }
}