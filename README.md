# Val-Vox

<p align="center">
  <img src="https://github.com/user-attachments/assets/d55a669f-c3a2-494b-964e-90924c4a936e" alt="Val-Vox Logo"  width="350" height="350"/>
</p>

<div justify-content="center">
<a align="center" href="https://creativecommons.org/licenses/by-nc/4.0/">
<img src="https://img.shields.io/badge/Project%20License-CC%20BY--NC%204.0-blue" alt="License CC BY-NC"/>
</a>
</div>

<p align="center">Val-Vox is a Python-based program designed to enable Valorant players to utilize automatic microphone detection within team voice chat. This functionality, originally restricted to Valorant's party chat feature, is now extended universally through Val-Vox, offering a lightweight solution for seamless communication during gameplay.</p>

## Installation and first execution

> 🚨
> Please use this project at your own risk. We cannot guarantee that it is 100% ban-proof, so please be aware of any potential risks, albeit very minimal, while using this tool.

1. Download the executable file from the releases tab.
2. Choose a directory of your preference and place the file there. Run the executable.
3. Note the number associated with your microphone used in Valorant, then close the command prompt.
4. Open the settings.txt file located in the same directory as the executable file and modify the "microphone" setting from null to the previously noted number. Ensure the comma remains after the number.
5. Optionally adjust [other settings in the file](#Settings), ensuring commas are correctly placed next to each value. 
6. Save and close the settings.txt file, then relaunch the executable.
7. Enjoy using the tool!

## Settings

Here is a list of the different settings you can adjust in the settings.txt file along with their function:
- "mute": Adjusts the key used for muting while the program is running.
- "microphone": Sets the microphone input used, ideally matching the one configured in Valorant.
- "threshold": Controls the activation sensitivity of the microphone, determining when the push-to-talk key is triggered in-game.
- "silence_duration": Sets a delay before releasing the push-to-talk key in-game based on the duration of silence detected.
- "muted_by_default": Enables instant muting upon program startup.

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
