from django.views import View
from django.http import JsonResponse
import json
from .models import CartItem
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# ShoppingCart class is used for adding and displaying cart
# For all methods, if there is an error an Internal Server Error 500 is return
# Cross-site request forgery (CSRF) attacks check is disable by this method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    # This method will add an item in the database
    # product_name,product_price,product_quantity are mandatory in the Json sent by the post method
    # If an invalid json structure is sent or no json at all, an exception message will be 
    # displayed to the user 
    def post(self, request):
        statusCode = 201
        try:
            data = json.loads(request.body.decode("utf-8"))
            p_name = data.get('product_name')
            p_price = data.get('product_price')
            p_quantity = data.get('product_quantity')

            product_data = {
                'product_name': p_name,
                'product_price': p_price,
                'product_quantity': p_quantity,
            }

            cart_item = CartItem.objects.create(**product_data)

            data = {
                "message": f"New item added to Cart with id: {cart_item.id}"
            }
        except Exception as err:
            statusCode = 500
            error = str(err)
            data = {
                    'message': f'Not able to add item exception: '+error
                }
        return JsonResponse(data, status=statusCode)

    def new_method(self):
        statusCode=500
        return statusCode

    # List all the items. If no item is available an empty json structure is sent 
    # and a No Content 204 code is also sent  
    def get(self, request):
        statusCode = 200
        try:
            items_count = CartItem.objects.count()
            items = CartItem.objects.all()

            items_data = []
            for item in items:
                items_data.append({
                    'id': item.id,
                    'product_name': item.product_name,
                    'product_price': item.product_price,
                    'product_quantity': item.product_quantity,
                })
            if items_count==0:
                statusCode = 204
            else:
                statusCode = 200

            data = {
                'items': items_data,
                'count': items_count,
            }
        except Exception as err:
            statusCode = 500
            error = str(err)
            data = {
                    'message': f'Not able to list item exception: '+error
                }
        return JsonResponse(data, status=statusCode)

# ShoppingCartUpdate classe is used for updating and deleting cart
# For all methods, if there is an error an Internal Server Error 500 is return
# For patch and delete the item id is place after update-item/
# Example of and item id 3 the Url will be
# http://127.0.0.1:8000/update-item/3
# Cross-site request forgery (CSRF) attacks check is disable by this method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):

    # If the item_id exists the product_quantity will be updated
    # The only parameter accepted will be product_quantity
    # Also there is no validation on the product_quantity attribute
    # If no json is sent an exception is generated
    def patch(self, request, item_id):
        statusCode = 200
        try:
            data = json.loads(request.body.decode("utf-8"))
            item = CartItem.objects.get(id=item_id)
            item.product_quantity = data['product_quantity']
            item.save()
            data = {
                'message': f'Item {item_id} has been updated'
            }
        except Exception as err:
            statusCode = 500
            error = str(err)
            data = {
                    'message': f'Error occur for item {item_id}. Update faild exception: '+error
                } 
        return JsonResponse(data, status=statusCode)

    # If the item_id exists the cart will be deleted 
    def delete(self, request, item_id):
        statusCode = 200
        try:
            item = CartItem.objects.get(id=item_id)
            item.delete()
            data = {
                'message': f'Item {item_id} has been deleted'
            } 
        except Exception as err:
            statusCode = 500
            error = str(err)
            data = {
                    'message': f'Error occur for item {item_id}. Delete faild exception: '+error
                }
        
        return JsonResponse(data, status=statusCode)
