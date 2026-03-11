import torch

#Giả sửa ảnh đọc từ Opencv: [H:224, W;224, Channels = 3]
cv2_image = torch.rand(224,224,3)
print("Kích tước ảnh từ Opencv:",cv2_image.shape)

#Cần chuyển số 3 từ vị trí trục 2 sang trục 0
#Trục cũ 0(H), 1(W), 2(C)
#Trục mới 2(C), 0(H), 1(W)

pytorch_images = cv2_image.permute(2,0,1)
print("Trục mơ sau khi xếp",pytorch_images.shape)
