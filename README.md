# ntuple-plagiarism-detection

A command line tool that performs plagiarism detection using N-tuple comparision algorithm allowing for synonyms in the text

### Prerequisites

Please use Python 3.1 or newer to run this program

### Running

Run the program by using:

```
python detect.py syns.txt file1.txt file.txt [tuple_len]
```
**Note *tuple_len* is an optional integer argument**

*detect.py* will return the percent tuples that *file1.txt* plagiarizes from *file2.txt*, including synonyms. 

## Design

The algorithm was designed as follows:

1) Hash the synonyms, using the first word as the value for the following synonyms.

   For example if *syns.txt* contains:
   
   ```
   run sprint jog
   ```
   it will produce the dictionary:
   ```
   {
       "sprint": "run",
       "jog": "run"
   }
   ```

2) Retrieve the tuples in *file2.txt*, replacing words that have synonyms with the default synonym

   For example if *file2.txt* contains:
   
   ```
   go for a jog
   ```
   with N = 3, it will produce the set:
   ```
   {
       ("go", "for", "a"),
       ("for, "a", "run")
   }
   ```
   **Note *jog* was replaced with *run***
   
 3) Retrieve the tuples in *file1.txt*, again replacing words that have synonyms with the default
 
    For example if *file1.txt* contains:
   
    ```
    go for a run
    ```
    with N = 3, it will produce the list:
    ```
    [("go", "for", "a"), ("for, "a", "run")]
    ```

4) Check how many tuples from *file1.txt* occur in *file2.txt* and return the percent value

   In the above example, 100% of the tuples in *file1.txt* occur in *file2.txt*, so we print 100% as the output

## Assumptions and Edge Cases
It was made sure that the tuple size was a valid input (i.e. greater than 0 and less than the file sizes). All the words were also stripped of punctuation and made lowercase. 
