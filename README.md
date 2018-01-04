 <p>This is another 'building-blocks-project', a Python script that searches a  root directory for a given keyword or regular expression present on any file name. Another file tests the script by creating a dummy directory.</p>
          <p> Assumptions:</p>
          <ul>
            <li> the user will enter a string or a complete regular expression (regex) to be located within the contents of all files in the chosen root_dir.</li>
            <li> Once a the first match is found in a file, that is counted as 1 (success).</li>
            <li>The final output is the number of successful matches (a maximum of one per file) for each subdirectory including the root_dir. </li>
            <li> The output is shown in two forms:</li>
              <ul>
                <li> as a Python dictionary where every key is a subdirectory path (including the root_dir), and corresponding values are the number of times the keyword was found on a file in that subdirectory.</li>
                <li>as a graph where each X is a subdir name string, and each corresponding Y represents the count values. </li>
              </ul>
            </ul>
