"""
==========================================================
MorphMotion AI
Body Part Selector
----------------------------------------------------------
Converts MediaPipe landmark IDs into meaningful
body part names.
==========================================================
"""


class BodyPartSelector:

    def __init__(self):

        # -----------------------------
        # Face Landmark Mapping
        # -----------------------------

        self.face_parts = {

            # Nose
            1: "NOSE",
            2: "NOSE",
            4: "NOSE",
            5: "NOSE",

            # Chin
            152: "CHIN",

            # Lips
            13: "UPPER_LIP",
            14: "LOWER_LIP",

            # Left Eye
            33: "LEFT_EYE",
            133: "LEFT_EYE",

            # Right Eye
            263: "RIGHT_EYE",
            362: "RIGHT_EYE",

            # Left Cheek
            234: "LEFT_CHEEK",

            # Right Cheek
            454: "RIGHT_CHEEK",

            # Forehead
            10: "FOREHEAD"
        }

        # -----------------------------
        # Pose Landmark Mapping
        # -----------------------------

        self.body_parts = {

            11: "LEFT_SHOULDER",
            12: "RIGHT_SHOULDER",

            13: "LEFT_ELBOW",
            14: "RIGHT_ELBOW",

            15: "LEFT_WRIST",
            16: "RIGHT_WRIST",

            23: "LEFT_HIP",
            24: "RIGHT_HIP",

            25: "LEFT_KNEE",
            26: "RIGHT_KNEE",

            27: "LEFT_ANKLE",
            28: "RIGHT_ANKLE",

            0: "HEAD"
        }

    # ---------------------------------------------------
    # Detect Face Part
    # ---------------------------------------------------

    def get_face_part(self, landmark_id):

        return self.face_parts.get(
            landmark_id,
            "UNKNOWN_FACE"
        )

    # ---------------------------------------------------
    # Detect Body Part
    # ---------------------------------------------------

    def get_body_part(self, landmark_id):

        return self.body_parts.get(
            landmark_id,
            "UNKNOWN_BODY"
        )

    # ---------------------------------------------------
    # Universal Selector
    # ---------------------------------------------------

    def identify(self, landmark):

        """
        landmark example

        {
            'id':234,
            'x':530,
            'y':320,
            'distance':14,
            'type':'face'
        }
        """

        if landmark is None:
            return None

        landmark_id = landmark["id"]

        if landmark["type"] == "face":

            return self.get_face_part(
                landmark_id
            )

        return self.get_body_part(
            landmark_id
        )