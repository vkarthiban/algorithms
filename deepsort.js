
data1 = {
    'c':'deff',
    'z':"gews",
    'd':"gbfihj",
    'a':[{'b':"oibhd","a":"hjdfn"}],
    'x' :[8,6,2,8,1,4]
}


function deepsort(data){
    var newobj = {}
    Object.keys(data).sort().map(function(key){
        if (Array.isArray(data[key]))
        {
            if(typeof data[key][0]==='object'){
                newobj[key] = []
                newobj[key].push(deepsort(data[key][0]))
            }
            else{
                newobj[key] = data[key].sort(function(a,b){return a-b;})
            }
        }
        else{
            newobj[key] =data[key]
        }
    })
    return newobj

}

console.log(deepsort(data1))

// deep sort function for sort all internal objects too//////////////////


data1 = {
    'c':'deff',
    'z':"gews",
    'd':"gbfihj",
    'a':{'b':"oibhd","a":"hjdfn"}
}
data2 = {
    'e':'xxxxx',
    'z':"secod",
    'y':"gbfihj",
    'a':{'b':"secod","a":"kkllklk"},
    'x' :[8,6,2,8,1,4]
}


function deepmerge(primary,secondary){
    Object.keys(secondary).map(function(key){
      if(primary[key]){
        if(typeof primary[key] == 'object')
        {
        primary[key]=deepmerge(primary[key],secondary[key])
        }
        else{
          primary[key] = secondary[key]
        }
      }
      else{
        primary[key] = secondary[key]
      }
    })
return primary
}


console.log(deepmerge(data1,data2))