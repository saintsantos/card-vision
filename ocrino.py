import cv2


def ocrino(template, dictionary):

    for x in dictionary:

        MIN_MATCH_COUNT = 10
        img = cv2.imread(''.join(["cards", "/", dictionary[x]["image_location"]]), 1)
        # w, h = template.shape[::-1]
        # print(''.join(["cards", "/", dictionary[x]["image_location"]]))
        card = ("error",)
        tapped = (0,)
        # account for tapping

        # Apply template Matching
        res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if (min_val < 0.005):
            # name of card goes here
            # print(min_val)
            print(x)
            # card = (x,)
            return card + tapped
        # print(min_val)
