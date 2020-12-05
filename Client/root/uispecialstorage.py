#search:
	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(self.SLOT_WINDOW_TYPE[self.categoryPageIndex]["window"], slotIndex)
		item.SelectItem(ItemVNum)
		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

#add:
		if app.ENABLE_SELL_ITEM:		
			if app.IsPressed(app.DIK_LCONTROL) and self.IsSellItems(slotIndex):
				self.__SendSellItemPacket(self.SLOT_WINDOW_TYPE[self.categoryPageIndex]["window"], itemSlotIndex)
				return
				
#search:
	def __SendMoveItemPacket(self, srcSlotWindow, srcSlotPos, dstSlotWindow, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMovePacket(srcSlotWindow , srcSlotPos, dstSlotWindow, dstSlotPos, srcItemCount)

#add:
	if app.ENABLE_SELL_ITEM:
		def IsSellItems(self, slotIndex):
			itemVnum = player.GetItemIndex(self.SLOT_WINDOW_TYPE[self.categoryPageIndex]["window"], slotIndex)
			item.SelectItem(itemVnum)
			itemPrice = item.GetISellItemPrice()
			
			# if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				# return True
				
			if itemPrice > 1:
				return True
				
			return False
			
		def __SendSellItemPacket(self, itemInvenType, itemVNum):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
				return
				
			net.SendItemSellPacket(itemInvenType, itemVNum)