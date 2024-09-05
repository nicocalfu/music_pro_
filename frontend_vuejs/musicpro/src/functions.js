import Swal from "sweetalert2";
import axios from "axios";
import Cookies from "js-cookie";

var user_id = '';

export function show_alerta(mensaje, icono, foco=''){
	if(foco !==''){
		document.getElementById(foco).focus();
	}
	Swal.fire({
		title:mensaje,
		icon:icono,
		customClass: {confirmButton: 'btn btn-primary', popup:'animated zoomin'},
		
	});
}

export function enviarSolicitud(metodo, parametros, url, mensaje){
	axios({method:metodo, url:url, data:parametros}).then(function(respuesta){
		var status = respuesta.data['status'];
		if(status){
			//sessionStorage.setItem('user_id', respuesta.data['user_id']);
			//window.location.href='/';
			console.log("funciona");
			return true;
		}else{
			console.log("no encontre usuario");
			return false;
		}
	}).catch(function(error){
		console.log("error")
		return false;
	});
}

export function removeUserCookie(){
	Cookies.remove('user_id');
	Cookies.remove('is_seller');
	Cookies.remove('is_admin');
	Cookies.remove('warehouseman');
}

export function getUserLogged() {
    return Cookies.get("user_id");
  }

export function setUserLogged(user_id) {
    Cookies.set("user_id", user_id);
  }

export function setUserSeller(is_seller) {
    Cookies.set("is_seller", is_seller);
  }

export function getUserSeller() {
    return Cookies.get("is_seller");
  }

export function setUserAdmin(is_admin) {
    Cookies.set("is_admin", is_admin);
  }

export function getUserAdmin() {
    return Cookies.get("is_admin");
  }

export function setWarehouseMan(warehouseman) {
    Cookies.set("warehouseman", warehouseman);
  }

export function getWarehouseMan() {
    return Cookies.get("warehouseman");
  }

export function getShoppingQuantity() {
    return Cookies.get("shopping_quantity");
  }

export function setShoppingQuantity(shopping_quantity) {
    Cookies.set("shopping_quantity", shopping_quantity);
  }

