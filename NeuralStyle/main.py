import mxnet as mximport model'''mxnet - gluon with tensorboard and mlflow1. mxboard 설명 (참고 : https://github.com/awslabs/mxboard)(참고 : https://github.com/awslabs/mxboard/blob/master/demo.md)MXBoard supports a set of Python APIs for logging the following data types for TensorBoard to render. Logging APIs for other languages may be added in the future.Graphs are visual representations of neural networks. MXBoard supports visualizing MXNet neural networks in terms of Symbol and HybridBlock.--> mxboard는 Symbol and HybridBlock 만 지원을 함실행 방법tensorboard --logdir=./logs --host=127.0.0.1 --port=88882. mlflow 설명'''# content_a  / style_b = 1/1000content_image = "content/chicago.jpg"style_image = "style/udnie.jpg"initial_noise_image = "content_image"  # or style image or noise -> Assigning an initial value to the content image is faster than assigning noise.image_size = (237, 356)  # height , width -> is expected to be at least 224.result = model.neuralstyle(epoch=1000, show_period=100, optimizer="adam", learning_rate=0.1, image_size=image_size,                           content_image=content_image, style_image=style_image, content_a=1, style_b=1000,                           initial_noise_image=initial_noise_image, ctx=mx.gpu(0), mxboard_savepath="mxboard")