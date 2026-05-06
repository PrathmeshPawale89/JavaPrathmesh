import java.util.HashMap;
import java.util.Map;

public class PR_1_B_WORDCOUNT {

    public static void main(String[] args) {

        // Big paragraph input
        String text = "Data science is an interdisciplinary field that uses scientific methods, "
                + "processes, algorithms, and systems to extract knowledge and insights from structured "
                + "and unstructured data. Data science combines mathematics, statistics, and computer "
                + "science to analyze large amounts of data. The goal of data science is to find patterns, "
                + "make predictions, and support decision making in various industries like healthcare, "
                + "finance, education, and technology.";

        // Convert text to lowercase for uniform counting
        text = text.toLowerCase();

        // Split words using space and punctuation handling
        String[] words = text.split("[\\s,\\.]+");

        // HashMap to store word frequency
        Map<String, Integer> wordCountMap = new HashMap<>();

        // Total word counter
        int totalCount = 0;

        // Map + Reduce logic (word counting)
        for (String word : words) {

            if (word.length() == 0) {
                continue;
            }

            totalCount++;

            if (wordCountMap.containsKey(word)) {
                wordCountMap.put(word, wordCountMap.get(word) + 1);
            } else {
                wordCountMap.put(word, 1);
            }
        }

        // Print word frequency result
        System.out.println("===== WORD COUNT RESULT =====\n");

        for (Map.Entry<String, Integer> entry : wordCountMap.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

        // Print total word count
        System.out.println("\n=============================");
        System.out.println("Total Number of Words: " + totalCount);
    }
}