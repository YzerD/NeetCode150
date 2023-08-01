# LC 832: Flipping an Image
# https://leetcode.com/problems/flipping-an-image/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is a n x n binary matrix named image.
    - What does our input tell us about it?
        With it being n x n, we know that it is a square. Knowing that it is
        also binary, we can expect that the values within the image is either
        a 0 or a 1.
    - What is our output?
        Our output is the image flipped horizontally, and then inverted, where
        we then return the resulting image
    - Can our image be empty?
        No, in the constraints the minimum dimensions our image can be is a 
        1 x 1 matrix
    - What does it mean to flip horizontally?
        Take [1,1,0] for instance, flipped horizontall results in [0,1,1]
    - What does it mean to be inverted?
        To inverted means to flip the bits, take [0,1,1], inverted it is now
        [1,0,0]


M-atch:
    I think for this problem, although probably not the most efficient solution
    we can break it down into smaller problems to tackle, that being the 
    flipping and the inverting. We can achieve this via two helper function.
    The flip will iterate through every row and I think there is some slicing
    of the index that flips the entire row, I think it's row[::-1]. Then our
    other helper will iterate through every row and column and see if it's a
    0, if so flip it 1, else flip it to 0. We can then call the helper 
    functions with the original image passed in.

P-lan:
    1) Declare our first helper function
    2) Iterating over every row
    3) Flip the rows horizontally using [::-1]
    4) Call the function
    5) Declare our second helper function
    6) Iterating over every row
    7) Iterating over every col
    8) If the element is a 0, flip it to 1
    9) Otherwise, it's a 1, flip it to 0
    10) Return the call of the invert function with the image passed in

I-mplement:
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Iterating over every row
        for i in range(len(image)):

            # Use the [::-1] trick to flip the row horizontally
            image[i] = image[i][::-1]

            # Iterating over every column
            for j in range(len(image[0])):

                # If the element is equal to 0
                if image[i][j] == 0:
                    # Flip the value to 1
                    image[i][j] = 1


                # Otherwise, it's equal to 1
                else:
                    # Flip the value to 0
                    image[i][j] = 0

        # Return the Resulting image
        return image


    def display(self, image: List[List[int]]) -> None:
        print(f"Input: image = {image}")
        print(f"Output:        {self.flipAndInvertImage(image)}\n")


# Testing
solution = Solution()


# Expects [[1,0,0],[0,1,0],[1,1,1]]
image = [[1,1,0],[1,0,1],[0,0,0]]
solution.display(image)


# Expects [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
solution.display(image)

"""
R-eview:
    - When first coding out the solution, I was declaring the helper function,
      I thought to myself, this is kinda uneccessary and scrapped the whole
      helper function idea.
    - Another thing that I realized when coding the solution is that, we can
      shorten down our code by including the flip within the nested loop and
      then perform the inversion 

E-valuate:
    - The runtime is O(n^2) since we have to check every element in the image
      in order to flip it
    - I think the runtime should be O(1) since we aren't using any auxilary
      data structure.
"""