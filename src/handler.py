from typing import  Dict, List, Any
import numpy as np
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, DDIMScheduler
import base64
from io import BytesIO


# set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# if device.type != 'cuda':
#     raise ValueError("need to run on GPU")

class EndpointHandler():
    def __init__(self, path=""):
        # load the optimized model
        self.scheduler = DDIMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", clip_sample=False, set_alpha_to_one=False)
        self.pipe = StableDiffusionPipeline.from_pretrained(path, scheduler=self.scheduler, safety_checker=None, torch_dtype=torch.float16)
        self.pipe = self.pipe.to(device)


    def __call__(self, data: Any) -> List[List[Dict[str, float]]]:
        """
        Args:
            data (:obj:):
                includes the input data and the parameters for the inference.
        Return:
            A :obj:`dict`:. base64 encoded image
        """
        inputs = data.pop("inputs", data)
        parameters = data.pop("parameters", None)
        self.generator.manual_seed(np.random.randint(low=52364)

        with autocast(device.type):
            if parameters:
              # pass custom parameters to model
                image = self.pipe(inputs, generator=self.generator, **parameters)["sample"][0]  
            else:
              # use default parameters if not defined
                image = self.pipe(inputs, num_inference_steps=20, guidance_scale=7.5, generator=self.generator)["sample"][0]
            
        # encode image as base 64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        # postprocess the prediction
        return {"image": img_str.decode()}