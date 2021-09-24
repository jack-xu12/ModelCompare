import torch
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_ft = torch.load('./squeezenet_hym_ft.pkl')
print(model_ft)