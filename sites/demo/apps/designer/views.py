from django.shortcuts import render
from django.conf import settings
from django.core.files import File
from oscar.core.loading import get_class, get_classes, get_model

ProductClass, Product, Category, ProductCategory = get_classes(
    'catalogue.models', ('ProductClass', 'Product', 'Category',
                         'ProductCategory'))

ProductImage = get_model('catalogue', 'productimage')


def create(request):
	context_dict = {}
	if request.method == 'POST':
		img_data = request.POST.get('imagesrc').decode("base64")
		img_file = open("./public/photo.jpg", "wb")
		img_file.write(img_data)
		img_file.close()

		#create a new product
		product_class = ProductClass.objects.get(pk=2)
		product = Product()
		product.product_class = product_class
		product.structure = Product.STANDALONE
		product.title = 'the first product'
		product.description = 'this is the first product'
		product.save()
		new_file = File(open('./public/photo.jpg', 'rb'))
		im = ProductImage(product=product, display_order=0)
		im.original.save('newtee.jpg', new_file, save=False)
		im.save()
		#save the image
		return render(request, 'designer/success.html')

	else:
		print 'else'
	
	return render(request, 'designer/create.html', context_dict)