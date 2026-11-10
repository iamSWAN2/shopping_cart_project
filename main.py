# 타이틀
def show_title():
    print("-"*60)
    print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*60)

# 제품 전체 목록
PRODUCTS = []

# 제품 객체 정의 
class Product:
    def __init__(self, name, number, price, inventory):
        self.name = name
        self.number = number
        self.__price = 0
        self.set_price(price) 
        self.__inventory = 0
        self.set_inventory(inventory)
        PRODUCTS.append(self)
    # 제품 가격 입력 캡슐화
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price >= 0:
            self.__price = price
    # 제품 재고 입력 캡슐화
    def get_inventory(self):
        return self.__inventory
    def set_inventory(self, inventory):
        if inventory >= 0:
            self.__inventory = inventory
    # def add_inventory(self, quantity):
    #     if quantity >= 0:
    #         current = self.get_inventory()
    #         self.set_inventory(current + quantity)

# 카트 객체 정의
class Cart:
    def __init__(self):
        self.products = {}
    # 장바구니에 담긴 물품 확인
    def show_in_cart(self):
        # 장바구니에 담긴 상품 총액
        cart_total_price = 0
        print("-"*60)
        for product in self.products:
            product_price = find_product(product).get_price()
            product_total_price = self.products.get(product, 0) * product_price
            cart_total_price += product_total_price
            print(f"{find_product(product).name}   x   {self.products.get(product, 0)}    {product_total_price}원")
        if not self.products:
            print("장바구니에 아무것도 담겨있지 않습니다.")
        print("-"*60)
        # 배송비 계산
        if not self.products:
            delivery_fee = 0
        else:
            if cart_total_price >= 30000:
                delivery_fee = 0
            else:
                delivery_fee = 3000
        # 결제금액
        final_price = cart_total_price + delivery_fee
        print(f"상품 합계                     {cart_total_price}원")
        print(f"배송비                     {delivery_fee}원")
        print(f"결제 금액                     {final_price}원")
    # 장바구니에 물품 추가
    def add_product(self):
        num = int(input("상품 번호 : "))
        # 제품 목록 중에서 없는 번호를 기입한 경우
        if find_product(num) is None:
            return print("장바구니에 없는 상품입니다.")
        # 제품 번호를 정상적으로 기입한 경우
        quantity = int(input("수량 : "))
        # 수량을 0보다 적게 기입한 경우
        if quantity <= 0:
            print("수량을 1개 이상 입력하세요.")
        total_quantity = self.products.get(num, 0) + quantity # 총 수량 계산
        # 수량이 제품 재고보다 많이 기입된 경우
        if quantity > find_product(num).get_inventory():
            print("수량이 재고보다 많습니다.")
        else:
            self.products[num] = total_quantity
            find_product(num).set_inventory(find_product(num).get_inventory() - quantity)
            print(f"{find_product(num).name} {total_quantity}개를 담았습니다.")
    # 장바구니의 물품 빼기
    def remove_product(self):
        num = int(input("상품 번호 : "))
        # 장바구니 내에 없는 번호를 기입한 경우
        if num not in self.products:
            print("장바구니에 없는 상품입니다.")
        # 장바구니에 있는 제품 번호를 기입한 경우
        quantity = int(input("수량 : "))
        # 수량을 0보다 적게 기입한 경우
        if quantity <= 0:
            print("수량을 1개 이상 입력하세요.")
        total_quantity = self.products.get(num, 0) - quantity # 총 수량 계산
        # 수량이 장바구니에 담긴 수량보다 많은 경우
        if quantity > self.products.get(num, 0):
            print("장바구니에 담겨진 수량을 확인해주세요.")
        else:
            self.products[num] = total_quantity
            find_product(num).set_inventory(find_product(num).get_inventory() + quantity)
            if self.products.get(num, 0) == 0:
                del self.products[num]
            print(f"{find_product(num).name} {quantity}개를 뺐습니다.")

        # for product in PRODUCTS:
        #     if product.number == num:
        #         current = product.inventory
        #         product.quantity = current
        #         print(f"{product.name} {product.quantity}개를 담았습니다.")
        #     else:
        #         self.__products = self.__products + product   
        #         print(f"{product.name} {product.quantity}개를 담았습니다.")
    # 장바구니 상품 합계
    # def get_subtotal(self):
    #     subtotal = 0
    #     for product in self.__products:
    #         subtotal += product.price * product.quantity
    #     return subtotal
# 제품 번호로 제품 객체 찾기
def find_product(num):
    for product in PRODUCTS:
        if product.number == num:
            return product
# 제품 목록 보여주기
def show_products():
    print("-"*60)
    for product in PRODUCTS:
        print(f"{product.number}.{product.name}     {product.get_price()}원    (재고 {product.get_inventory()}개)")

product1 = Product("무선 이어폰", 1, 89_000, 3)
product1 = Product("텀블러", 2, 15_000, 10)
product1 = Product("보조배터리", 3, 32_000, 5)
product1 = Product("마우스패드", 4, 9000, 0)
product1 = Product("USB허브", 5, 18_000, 4)

cart = Cart()

# 메뉴 선택시 발생하는 메소드 또는 함수
def handle_menu(num):
    if num == 1:
        return show_products()
    elif num == 2:
        return cart.add_product()
    elif num == 3:
        return cart.remove_product()
    elif num == 4:
        return cart.show_in_cart()


def main():
    show_title()
    while True:
        choice_menu = input("선택 : ")
        if choice_menu.isdigit():
            if 0 < int(choice_menu) < 5:
                handle_menu(int(choice_menu))
                print("\n")
                show_title()
            elif 4 < int(choice_menu) < 8:
                print("아직 구현되지 않은 기능입니다.")
                print("\n")
                show_title()
            else:
                print("메뉴 목록 안의 숫자 또는 알파벳을 입력해주세요.")
                print("\n")
                show_title()
        else:
            if choice_menu == "q":
                print("종료합니다.")
                break


main()


# show_title()


# cart1 = Cart()


# print(cart1.add_product())
# print(find_product(1).get_inventory())

# print(cart1.remove_product())
# print(find_product(1).get_inventory())

# cart1.show_in_cart()
# show_products()