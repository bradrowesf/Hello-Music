"""Player Class, v2"""

import os
from scamp import Session
from scamp import wait


class Player:
    """The thing that plays the notes"""

    def __init__(self):

        # Create and configure the session and part.
        self.session = Session(tempo=120)
        self.part = self.session.new_part("Clarinet")

        # Set initial config values
        self.pause = 2
        self.volume = 1
        self.duration = 1
        self.trial_sets = []

    def set_trial_sets(self, trial_sets):
        """Feed the list of trial sets to the player"""

        self.trial_sets = trial_sets

    def pre_roll(self):
        """Pause before start of playing"""

        # Wait for the user to press a key to begin
        input("Press ENTER to begin trial set...")

        # Wait so the first note isn't clipped
        wait(self.pause)

    def play(self, pause=False):
        """Play the notes defined in the trial_sets list"""

        # Iterate through the trial sets.
        trial_set_index = 0
        for trial_set in self.trial_sets:
            trial_set_index += 1
            print(f"Trial #{trial_set_index} of {len(self.trial_sets)}")
            print(
                "SOMETHING HERE TO EXPLAIN WHAT'S IN THESE TRIALS (I.E. KEY/MODE/RANGE/ETC.")

            self.pre_roll()

            # Iterate through the trials.
            trial_index = 0
            for trial in trial_set:
                trial_index += 1
                print(f"---- {trial_index}/{len(trial_set)}")

                # Play through all the notes in the trial.
                for note in trial:
                    self.part.play_note(note, self.volume, self.duration)

                # If option selected, wait for a key press before next trial.
                if pause:
                    os.system('pause')

                wait(self.pause)    # Pause before the next trial
