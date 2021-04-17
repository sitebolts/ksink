#Some websites have memory leak issues where staying on the same browser tab for a while will gradually eat up the browser's memory until it crashes
#As a workaround, you can switch to a new tab every so often
def replace_current_tab_with_blank_tab(driver):
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def get_element_value(parent_element, selection_method, selector, value_type):
    element_value = ''
    element = None

    try:
        if (selection_method == None):
            element = parent_element
            pass
        elif (selection_method == 'css'):
            element = parent_element.find_element_by_css_selector(selector)
            pass
        elif (selection_method == 'xpath'):
            element = parent_element.find_element_by_xpath(selector)
            pass
        else:
            element_value = ''
    
    except NoSuchElementException:
        element = None
    
    if (element != None):
        try:
            if (value_type == 'text'):
                element_value = element.text
            elif (value_type == 'value'):
                element_value = element.get_attribute('value')
            elif (value_type == 'href'):
                element_value = element.get_attribute('href')
            elif (value_type == 'inner_html'):
                element_value = element.get_attribute('innerHTML')
            elif (value_type == 'outer_html'):
                element_value = element.get_attribute('outerHTML')
            elif (value_type == 'select'):
                element_value = Select(element).first_selected_option.text
            elif (value_type == 'is_selected'):
                element_value = str(element.is_selected())
            else:
                element_value = ''

        except AttributeError:
            element_value = ''

    return element_value


def get_iframe_html(driver, css_selector):
    iframe_html = ''

    try:
        driver.switch_to.frame(driver.find_element_by_css_selector(css_selector))
        iframe_html = driver.find_element_by_tag_name("body").get_attribute('innerHTML')
        driver.switch_to.default_content()

    except NoSuchElementException:
        iframe_html = ''

    return iframe_html
