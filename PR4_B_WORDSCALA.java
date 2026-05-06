import java.util.HashMap;
import java.util.Map;

public class PR4_B_WORDSCALA {

    public static void main(String[] args) {

        // Sample text
        String text = "big data analytics big data spark";

        // Convert to lowercase
        text = text.toLowerCase();

        // Split words
        String[] words = text.split(" ");

        // HashMap for counting words
        HashMap<String, Integer> wordCount = new HashMap<>();

        // Count words
        for (String word : words) {

            if (wordCount.containsKey(word)) {

                wordCount.put(word,
                        wordCount.get(word) + 1);

            } else {

                wordCount.put(word, 1);
            }
        }

        // Display result
        System.out.println("Word Count:\n");

        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {

            System.out.println(entry.getKey()
                    + " : " + entry.getValue());
        }
    }
}