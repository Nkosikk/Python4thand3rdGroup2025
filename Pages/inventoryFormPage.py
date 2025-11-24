from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryFormPage:

    webAutomationAdvanceTab_xpath="//span[contains(@class, 'tab-label') and contains(text(), 'Web Automation Advance')]"


    rdn_standardRadioButton_xpath = "//input[contains(@type, 'radio') and contains(@value, 'standard') and contains(@name, 'shippingMethod')]"


    rdn_expressRadioButton_xpath ="//input[contains(@type, 'radio') and contains(@value, 'express') and contains(@name, 'shippingMethod')]"



    rdn_warrantyNoneRadioButton_xpath ="//input[contains(@type, 'radio') and contains(@value, 'none') and contains(@name, 'warranty')]"


    rdn_warrantyOneYearRadioButton_xpath ="//input[contains(@type, 'radio') and contains(@value, '1yr') and contains(@name, 'warranty')]"



    rdn_warrantyTwoYearsRadioButton_xpath ="//input[contains(@type, 'radio') and contains(@value, '2yr') and contains(@name, 'warranty')]"


    btn_viewInvoiceButtonOnPopUp_xpath ="//button[contains(@title, 'View Invoice History') and contains(text(), 'View Invoice')]"



    btn_viewButtonInsidePopUp_xpath ="//button[contains(text(), 'View') and contains(@style, 'linear-gradient')]"



    btn_closeModalButton_xpath ="//button[contains(text(), '✕') and contains(@style, 'font-size: 24px')]"



    ddl_DeviceType_id = "deviceType"


    ddl_Brand_id ="brand"


    ddl_Color_id ="color"


    rdn_storage64Gb_id ="storage-64GB"


    rdn_storage128Gb_id="storage-128GB"


    rdn_storage256Gb_id="storage-256GB"


    txt_quantityField_id ="quantity"



    txt_addressField_id ="address"


    btn_inventoryNextButton_id ="inventory-next-btn"



    txt_discountCodeField_id="discount-code"

    btn_applyDiscountButton_id ="apply-discount-btn"


    btn_reviewCartButton_id="review-cart-btn"


    btn_confirmPurchaseButton_id ="purchase-device-btn"

    btn_logoutButton_xpath="//button[contains(@class, 'logout-btn') and contains(text(), 'Logout')]"


    btn_confirmCartButton_id="confirm-cart-btn"


    btn_addToCartButton_id ="add-to-cart-btn"


    txt_discountFeedbackText_id ="discount-feedback"



    def __init__(self, driver):
        self.driver = driver

    def verifyInventoryFormPageHeading(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.webAutomationAdvanceTab_xpath)))
        element.is_displayed()