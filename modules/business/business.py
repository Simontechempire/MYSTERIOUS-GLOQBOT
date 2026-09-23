class BusinessSuite:

    def create_customer(self, name: str):
        return {
            "name": name,
            "status": "new",
        }

    def create_business_task(self, title: str):
        return {
            "title": title,
            "status": "pending",
        }

    def create_report(self, title: str, data: dict):
        return {
            "title": title,
            "data": data,
        }


business_suite = BusinessSuite()
