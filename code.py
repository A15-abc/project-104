import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Add text for each planet
cv2.putText(img, "Mercury", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Venus", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Earth", (350, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Mars", (500, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Jupiter", (650, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Saturn", (800, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Uranus", (950, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Neptune", (1100, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the image
cv2.imshow("output", img)

# Wait for a key press
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)