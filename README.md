# Val-Vox

<p align="center">
  <img src="https://github.com/user-attachments/assets/d55a669f-c3a2-494b-964e-90924c4a936e" alt="Val-Vox Logo"  width="350" height="350"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Code%20License-GPL%20v3-darkgreen" alt="License GPLv3" href="https://www.gnu.org/licenses/quick-guide-gplv3.en.html"/>
  <img src="https://img.shields.io/badge/Text%20License-CC%20BY--SA%204.0-blue" alt="License CC BY-SA"/>
</p>

<p align="center">Val-Vox is a Python-based program designed to enable Valorant players to utilize automatic microphone detection within team voice chat. This functionality, originally restricted to Valorant's party chat feature, is now extended universally through Val-Vox, offering a lightweight solution for seamless communication during gameplay.</p>

## Installation and first execution

> 🚨
> Please use this project at your own risk. We cannot guarantee that it is 100% ban-proof, so please be aware of any potential risks, albeit very minimal, while using this tool.

1. Download the executable file from the releases tab.
2. Choose a directory of your preference and place the file there. Run the executable.
3. Note the number associated with your microphone used in Valorant, then close the command prompt.
4. Open the settings.txt file located in the same directory as the executable file and modify the "microphone" setting from null to the previously noted number. Ensure the comma remains after the number.
5. Optionally adjust other settings in the file, ensuring commas are correctly placed next to each value.
6. Save and close the settings.txt file, then relaunch the executable.
7. Enjoy using the tool!

## Dependencies

Alternatively, you can opt to download the source code of the project and utilize the main.py file instead of the executable version. If you choose this option, install the following dependencies to ensure the project functions properly:
- os
- json
- pyaudio
- numpy
- pynput
- time
- sys
- colorama

## Sources

- The project's logo features the Valorant font style for the letter "V".
- The muting and unmuting sounds were created using the Chrome Music Lab.

## Licenses

For more information about the licensing of this project, please refer to the badges at the very top of this documentation.
